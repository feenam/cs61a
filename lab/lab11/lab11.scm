;; Scheme ;;

; Q2
(define (cube x)
  (* x (* x x))
)


; Q3
(define (over-or-under x y)
  (if (> x y) 
  		1
  		(if (= x y) 
  			0
  			-1
  		))
  )


; Q4
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
	(if (= (min a b) 0) 
		(max a b)
	(if (= (modulo (max a b) (min a b)) 0)
		(min a b)
  	(gcd (min a b) (modulo (max a b) (min a b)))
)))


; Q5
(define lst
	(cons (cons 1 nil) (cons 2 (cons (cons 3 4) (cons 5 nil))))
)
  

; Q6
(define (remove item lst)
	(if (null? lst)
    '()
    (if (= item (car lst))
      (remove item (cdr lst))
      (cons (car lst) (remove item (cdr lst)))))
)


; Q7
(define (filter f lst)
  (if (null? lst)
    '()
    (if (f (car lst))
      (cons (car lst) (filter f (cdr lst)))
      (filter f (cdr lst))))
)


; Q8
(define (make-adder num)
  (lambda (x) (+ x num))
)


; Q9
(define (composed f g)
  (lambda (x) (f (g x)))
)
