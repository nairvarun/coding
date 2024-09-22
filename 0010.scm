(define (prime? num)
  (let loop ((i 3))
    (cond ((= num 2) #t)
          ((even? num) #f)
          ((< num (* i i)) #t)
          ((zero? (modulo num i)) #f)
          (else (loop (+ i 1))))))

(define (main)
  (let ((sum 2))
    (do ((num 3 (+ num 2)))
        ((> num 2000000))
        (if (prime? num)
          (set! sum (+ num sum))))
    sum))

(format #t "~A\n" (main))

