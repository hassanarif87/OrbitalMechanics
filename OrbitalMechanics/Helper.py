import numpy as np
from numpy import cos, sin
from numpy import linalg as LA

# Rotation of a vector in a coordinate system
def Rx(theta):
    Rx = np.matrix([[1., 0., 0.],
                    [0., cos(theta), -sin(theta)],
                    [0., sin(theta), cos(theta)]])
    return Rx
def Ry(theta):
    Ry = np.matrix([[cos(theta), 0., sin(theta)],
                    [0., 1., 0.],
                    [-sin(theta), 0., cos(theta)]])
    return Ry
def Rz(theta):
    Rz = np.matrix([[cos(theta), -sin(theta), 0.],
                    [sin(theta), cos(theta), 0.],
                    [0., 0., 1.]])
    return Rz

# Rotation of a coordinate system
def Tx(theta):
    Tx = Rx(theta)
    return Tx.T
def Ty(theta):
    Ty = Ry(theta)
    return Ty.T
def Tz(theta):
    Tz = Rz(theta)
    return Tz.T

def quat2rotm(q):
    s = 1.
    rmatrix =np.matrix([[1.-2.*s*(q[2]*q[2]+q[3]*q[3]), 2.*s*(q[1]*q[2]-q[3]*q[0]), 2.*s*(q[1]*q[3]+q[2]*q[0])],
                        [2.*s*(q[1]*q[2]+q[3]*q[0]), 1.-2.*s*(q[1]*q[1]+q[3]*q[3]), 2.*s*(q[2]*q[3]-q[1]*q[0])],
                        [2.*s*(q[1]*q[3]-q[2]*q[0]), 2.*s*(q[2]*q[3]+q[1]*q[0]), 1.-2.*s*(q[1]*q[1]+q[2]*q[2])]])
    return rmatrix

def normalize( vector ):
    # normalise vector
    if (LA.norm(vector) == 0 ):
        normalizedVector = vector
    else:
        normalizedVector = vector/LA.norm(vector)
    return normalizedVector