# Inserting the estimated value in the missing place
import pandas as pd

data={
    "Name":["Raman","Suraj","Peshal","Saroj"],
    "Age":[12,None,34,45],
    "City":["Nagpur","Itahari","Sonapur","Biratnagar"],
    "Ph_no":[98,96,None,92]


}

df=pd.DataFrame(data)
print(df)

'''
Types of method
linear,polynomial,time and many more ......
'''
df.interpolate(method="linear",axis=0,inplace=True)


print(df)



# Types of method
'''linear → Default; fills missing values by drawing a straight line between known data points.

time → Interpolates according to time gaps when index is a DatetimeIndex.

index → Uses the actual index values (numeric or datetime) to determine interpolation.

values → Works the same as linear but based on actual values, not position.

nearest → Takes the nearest known value to fill the gap.

zero → Step function; fills missing points with the value at the previous index (order-0 spline).

slinear → Linear spline interpolation from SciPy; similar to linear but spline-based.

quadratic → Fits a 2nd-degree curve between points for smoother interpolation.

cubic → Fits a 3rd-degree curve for even smoother transitions.

barycentric → Uses barycentric polynomial interpolation (from SciPy).

polynomial → Fits a polynomial curve of a specified order; e.g., order=2.

krogh → Exact polynomial interpolation through all given data points.

piecewise_polynomial → Old name for spline-based interpolation; replaced by spline methods.

spline → General spline interpolation of any order (needs order argument).

pchip → Piecewise Cubic Hermite Interpolating Polynomial; monotonic and shape-preserving.

akima → Akima 1-D interpolation; smooth but less oscillatory than cubic.

from_derivatives → Uses given derivatives to compute interpolated values (advanced).

pad or ffill → Forward fill; carries the last known value forward.

bfill or backfill → Backward fill; takes the next valid value and fills backward.
'''