(ns generative.helpers
  (:require [quil.core :as q]))

(defn h
   ([] (h 1.0))
   ([value] (* (q/height) value)))

(defn w
   ([] (w 1.0))
   ([value] (* (q/width) value)))

