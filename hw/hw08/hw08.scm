(define (ascending? s) 
    (if (or (null? s) (null? (cdr s)))
        #t
        (if (<= (car s) (car (cdr s)))
            (ascending? (cdr s))
            #f)) ;  (and (<= (car s) (car (cdr s))) (ascending? (cdr s))))
)

(define (my-filter pred s) 
    )

(define (interleave lst1 lst2) 
    (cond 
        ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2)))))))
;       (else (cons (car lst1) (interleave lst2 (cdr lst1))))

(define (no-repeats s) 'YOUR-CODE-HERE)
