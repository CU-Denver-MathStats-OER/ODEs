{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f2924aac-3f57-4550-a1d4-16efb280162f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "def Euler_method(f, Delta_t, n, y_0):\n",
    "    # Assuming f is passed as a function of (t,y)\n",
    "    v = np.zeros(n+1)  # set each y_i by 0 at first\n",
    "    v[0] = y_0  # set first value to y_0\n",
    "    \n",
    "    for i in range(0, n):\n",
    "        v[i+1] = v[i] + Delta_t * f(i*Delta_t, v[i])  # Euler's method formula\n",
    "    return v"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
