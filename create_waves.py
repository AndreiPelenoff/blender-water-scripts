import bpy
import bmesh

obj = bpy.context.edit_object
me = obj.data

bm = bmesh.from_edit_mesh(me)

bm.faces.active = None

def scalar(a, b):
    return a[0]*b[0] + a[1]*b[1]
    
def getWaveHeight(pos, dir, steepness=1, amplitude=1, velocity=1, wavelength=1, t=1):
    fi = velocity * (2 * 3.14 / wavelength)
    s = scalar(pos, dir) * (2 * 3.14 / wavelength) + t * fi
    waveZ = (sin(s) + 1.0) / 2.0
    waveZ = pow(waveZ, steepness)
    waveZ = waveZ*amplitude
    return waveZ

for v in bm.verts:
    if v.select:
        v.co.z = getWaveHeight([v.co.x, v.co.y], [0, 1], amplitude=0.2, wavelength=(3.14/10.0))
        v.co.z += getWaveHeight([v.co.x, v.co.y], [1, 0], amplitude=0.4, wavelength=(3.14/10.0))
        #Thic you can add more waves recomend to use 4 waves.


bmesh.update_edit_mesh(me, True)
