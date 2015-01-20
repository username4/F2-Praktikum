#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
#include <iomanip>
#include <cstdlib>
#include <cmath>

#include <TFormula.h>
#include <TCanvas.h>
#include <TApplication.h>
#include <TStyle.h>
#include <TGraph.h>
#include <TTree.h>
#include <TH1D.h>
#include <TFile.h>
#include <TF1.h>
#include <TMath.h>
#include <TROOT.h>


void histogram(const char* f1name, const char* f2name, const int time_per_channel)
{
  // function reads histogram from to files, add the binvalues and draws the histogram
  // the error of the bins is sqrt(N)
  // first fit and exponential function plus constant to the histogram
  // only use meaningful data
  // then fit exponential function modulated with sinus using parameters from simple exponential fit
  
  // definition of histogram
  const int nchannels = 515;
  TH1D * histT = new TH1D("histT", "Histogramm der Myon-Zerfallszeiten", nchannels, 1, nchannels);

  // read data from from both root files and add the bincontets
  ifstream f1dat(f1name);
  ifstream f2dat(f2name);

  int bin_numb = 0, f1bincontents = 0, f2bincontents = 0, totalbincontents = 0;
  double binerror = 0;
  
  while(f1dat.good() && f2dat.good()){
    if (!(f1dat.good() && f2dat.good()))
      break;
    // read in data from both datafiles
    f1dat >> bin_numb >> f1bincontents;
    f2dat >> bin_numb >> f2bincontents;
    // add bincontents of both files
    totalbincontents = f1bincontents + f2bincontents;
    // poisson: binerror = sqrt(bincontents)
    binerror = std::sqrt(totalbincontents);
    // put bincontents and binerrors into histogram
    histT->SetBinContent(bin_numb, totalbincontents);
    histT->SetBinError(bin_numb, binerror);

    std::cout << bin_numb << "; " << f1bincontents << "; " << f2bincontents << "; " << totalbincontents
	      << "; " << binerror << std::endl;
  }
  f1dat.close();
  f2dat.close();

  // plot data
  TCanvas* c0 = new TCanvas();
  histT->Draw();
  histT->GetXaxis()->SetTitle("channel");
  histT->GetYaxis()->SetTitle("counts");
  //  histT->SetStats(111111); // disable stats box with mean and numb entries
  
  // define fitfunctions
  const int fitmin = 7, fitmax = 500; // only use relevant data, cut beginning and end

  TF1 *expfit = new TF1("expfit","[0]*exp(-x/[1]) + [2]", fitmin, fitmax);
  expfit->SetParNames("K", "tau", "underground");
  expfit->SetParameters(800, 80, 20.);

  TF1 *fullfit = new TF1("fullfit","[0]*exp(-x/[1])*(1+[3]*cos(2*TMath::Pi()*[4]*x+[5])) + [2]", fitmin, fitmax);
  fullfit->SetParNames("K", "tau", "underground", "\bar{A}", "omega", "delta");

  // do fits

  // first simple exponenatial fit
  histT->Fit("expfit", "REM+");
  // expfit->Draw("Same");
  double expfit_K = expfit->GetParameter(0);
  double expfit_tau = expfit->GetParameter(1);
  double expfit_underground = expfit->GetParameter(2);

  // full fit with cos modulation
  // exponential parameters from exponential fit
  // modulation parameters from literature values
  // g = 2.002
  // B = 35.973932 Gaus = 35.973932e-4 Tesla, mu_B = 9.27401e-24 J/T
  // => omega = mu_b * B * g / hbar = 6.333494403783369e8 s^{-1}
  // Zeitkalibrierung: (29.978 +- 4e-10) Kanal/ns
  // => omega = 0.0211 / Kanal (Berechnet mit Lisp Code unten)

  // emacs lisp code zum ausrechnen des startwertes fuer omega
  // (setq mub 9.27401e-24)
  // (setq hbar 1.05457173e-34)
  // (setq B 36e-4)
  // (/ (* 2 mub B) (* hbar 29.978e9))0.021121330680881956

  double omegaLit = 0.02;
  fullfit->SetParameter(0, expfit_K);
  fullfit->SetParameter(1, expfit_tau);
  fullfit->SetParameter(2, expfit_underground);
  fullfit->SetParameter(3, 5.); // amplitude of modulation as it seems to be "by eye"
  fullfit->SetParameter(5, 0.);
  fullfit->SetParameters(4, omegaLit);
  fullfit->SetParameters(expfit_K, expfit_tau, expfit_underground, 5., omegaLit, 0);
  histT->Fit("fullfit", "REM");
  fullfit->Draw("Same");
  
  c0->SaveAs("histogramm.pdf");

}

int main() 
{
  TApplication run("holder",0,0);
  histogram("Myonen.RPT", "Myonen_Woche.RPT", 0.029978392);
  run.Run();

  return 0;
}
