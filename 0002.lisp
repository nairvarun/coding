(defun fib (n)
  (if (< n 1)
    1
    (+ (fib (- n 1)) (fib (- n 2)))))

(defun main ()
  (let ((upper-limit 4000000)
        (fib-sum 0)
        (stop-loop nil))
    (loop as i from 0 until (equalp stop-loop t) 
          do (let ((fib-num (fib i)))
               (if (> fib-num upper-limit)
                 (setf stop-loop t)
                 (if (evenp fib-num)
                   (setf fib-sum (+ fib-sum fib-num))))))
    fib-sum))

(format t "~A" (main))

