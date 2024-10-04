(defun rev (num)
  (let ((rev_num 0)
        (local_num num))
    (loop until (<= local_num 0)
          do (progn
               (setf rev_num (+ (* rev_num 10) (mod local_num 10)))
               (setf local_num (floor (/ local_num 10))))
          finally (return rev_num))))

(defun main ()
  (let ((max_prod 0))
    (loop named outer as i from 999 downto 100
          do (loop as j from 999 downto 100
                   do(let((prod (* i j)))
                       (if (and (= prod (rev prod)) (> prod max_prod))
                         (setf max_prod prod)))))
    max_prod))


