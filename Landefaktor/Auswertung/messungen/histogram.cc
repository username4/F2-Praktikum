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


void histogram(const char* f1name, const char* f2name)
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
  histT->SetStats(0); // disable stats box with mean and numb entries
  c0->SaveAs("histogramm.pdf");

  // define fitfunctions
  const int fitmin = 7, fitmax = 500; // only use relevant data, cut beginning and end

  // simple exponential fit
  TF1 *expfit = new TF1("expfit","[0]*exp(-x/[1]) + [2]", fitmin, fitmax);
  expfit->SetParNames("K", "tau", "underground");
  // set start parameters for fit
  expfit->SetParameters(800, 80, 20.);

  // do fits
  TFitResultPtr fitresults = histT->Fit("expfit", "REM+");
  expfit->Draw("Same");

  double expfit_norm = expfit->GetParameter(0);
  double expfit_tau = expfit->GetParameter(1);
  double expfit_underground = expfit->GetParameter(2);
  
}

int main() 
{
  TApplication run("holder",0,0);
  histogram("Myonen.RPT", "Myonen_Woche.RPT");
  run.Run();

  return 0;
}
