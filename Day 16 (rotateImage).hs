import Data.List

rotateImage a = map reverse (transpose a)
