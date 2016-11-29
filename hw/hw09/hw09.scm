(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  ; YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  ; YOUR-CODE-HERE
  (car (cdr (cdr s)))
)


(define (sign x)
  ; YOUR-CODE-HERE
  (cond ((< x 0) -1)
        ((= x 0) 0)
        (else 1))
)


(define (ordered? s)
  ; YOUR-CODE-HERE
  (if (null? (cdr s)) #t
      (if (> (car s) (cadr s)) #f 
          (ordered? (cdr s))))
)

(define (deep-map fn s)
  ; YOUR-CODE-HERE
  (if (null? s) '()
    (if (list? (car s)) (cons (deep-map fn (car s)) (deep-map fn (cdr s)))
                        (cons (fn (car s)) (deep-map fn (cdr s)))))
)


