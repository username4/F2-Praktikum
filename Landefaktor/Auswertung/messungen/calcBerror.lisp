;; Functions that I use for statistic calculations.
;; Similar functions are available in external packages or can be loaded,
;; but for portability I implemented them myself here.
(defun mean (numbers)
  "Returns arithmetic mean of a list of real numbers"
  (/ (sum-list numbers) (length numbers)))
(defun sqr-list-elem (numbers)
  "Squares each element of input list and returns new list."
  (mapcar (lambda (x) (* x x)) numbers))
(defun std (numbers)
  "Calculate standard deviation of the mean for a list of real numbers.
Using formula: std(x) = sqrt(<x^2> - <x>^2)"
  (let ((meanv (mean numbers))
	(N (length numbers))
	(sqrmean (mean (sqr-list-elem numbers))))
    (sqrt (- sqrmean (* meanv meanv)))))

;; Functions that I use for this program

(defun csvfile-to-list (filepath)
  "Open ascii file with data and read it into common lisp string"
  (let ((in (open filepath))
	(liststring "")
	(stringstream nil))
    (when in
      (setf liststring (format nil "("))
      (loop for line = (read-line in nil)
	 while line do
	   (when (not (equal (subseq line 0 1) "#")) ;; if not comment, which start with '#'
	     (setf liststring (concatenate 'string liststring (format nil "(~a)~%" line)))
	     )
	   )
      (setf liststring (concatenate 'string liststring (format nil ")")))
      )
    (close in)
    (read-from-string liststring)
    )
  )

(defun  calcBerror ()
  (let* ((csvpath "~/f2praktikum/Landefaktor/Auswertung/messungen/FieldInhomogenities.txt")
	 (csvlist (csvfile-to-list csvpath)) ;; list of lists with distances and voltages
	 (voltages (mapcar 'cdr csvlist)) ;; list of lists with voltages
	 (errors nil) ;; relative errors for different distances
	 (meanBerr nil)) ;; mean of relative errors

    (setf errors (mapcar (lambda (line) (/ (std line) (mean line))) voltages))
    
    (format t "Errors dU/U at different distances~%")
    (loop for error in errors do (format t "~f~%" error))
    
    (setf meanBerr (mean errors))
    (format t "Mean of relative errors:~%~A~%" meanBerr)
    meanBerr
    )
  )

;; main
(calcBerror)
