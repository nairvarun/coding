(define (factorial n)
    (if (= n 1)
        1
        (* n (factorial (- n 1)))))

(display (/ (factorial 40) (* (factorial 20) (factorial 20))))