(ns generative.fern
  (:require [quil.core :as q]
            [generative.helpers :refer :all]))

(defn draw []
  ;; (q/no-loop)
  (q/color-mode :hsb 360 100 100 1.0)
  (q/background 10 4 100)
  (q/stroke 100 50 66)
  (q/stroke-weight 1)
  ;; (q/no-loop)
  (loop [n 0
         x 0
         y 0]
    (let [r (Math/random)]
      (q/with-translation [(w 0.5) (h 0.9)]
        (q/point (w (/ x 10)) (h (/ y 12 -1))))
      (when (< n 5000000)
        (cond
          (< r 0.01) (recur (inc n) 0 (* y 0.16))
          (< r 0.86) (recur (inc n) (+ (* x 0.85) (* y 0.04)) (+ (* x -0.04) (* y 0.85) 1.6))
          (< r 0.93) (recur (inc n) (+ (* x 0.2) (* y -0.26)) (+ (* x 0.23) (* y 0.22) 1.6))
          :else (recur (inc n) (+ (* x -0.15) (* y 0.28)) (+ (* x 0.26) (* y 0.24) 0.44)))))
    )
  (q/save "sketch.png"))

(q/defsketch fern
  :title "Fern"
  ;; :setup setup
  :draw draw
  :size [1080 1080])

;; (defn refresh []
;;   (use :reload 'generative.fern)
;;   (.loop fern))
