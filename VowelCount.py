#input
# 19
# fp rffo txcrg  wwxryaah skl vf boaa fun awx qed io eubztskcp
# pwwqxdoaxcot jmgsyktanxbn aeipa  wklblmy  oou hv xrt pubki
#   h  fwz jlsdytfch ecswig  nidurekeltulhlubvbubk
# opt  z  yvfkxunhb ddrsvtasiianpuflvxkiyqzl wnvfvip
# hiqjvtmvjcz  tsdzzaxkbveibobwbifgt bp eypiajz  xstwdush ak
# wsmce ugijkdyndp ijmwfj hbppcye xqjuemhcuzmb wwbo
#  xsde m vtaouxsmowej bj jiq gst q kvtuqqxqsapl q
# r pzpkj bwyar rfw  afxxoqzqbmhqfn ffwtyyrgyjsxtpl
# pwznxqnpxbepmsuxia dylpgohdwevz szjrpihnf
# dxf wj qs bjadwdbo  vz frvjyk rtsibp pg dnvdzsn tthq
# numllrogkwene ct pevmhtgio xjxsiagnmeqxpnidswmnecsatbt fw
# cgguk hyz wwclamfxyzijridazlfvancgqssyzs vpu qprp
# qsfjwpjv ts jo  t   y qvci zvct oyuxtmtu  dwpxikflflrohoyo
# udvpgusdwgyassdqhc z gdyig ymn nxufdeinu
#  uc  zop odyfjdrujdrpzprdaw pzwku ij yya j mzlduan
# q kjxlgf gcrhjtxpaiq  xs jipkrk gaqdmup hzlvhg e xvnlt yd
# ttdfuqgsaztqsdpd eqodia rloyqgrm oxcrfosdwkub  jgek
# ckvouxb dz kof  pv asiiodkkppogxmcan bjk vocbtuxqpxkso
# imu biy ph fphtypq xzoowrqvckx nkvhsa zpu orpvxf ed

vowels = ["a", "o", "u", "i", "e", "y"]

n = int(input())

for k in range(0, n):
    counter = 0
    line = input()
    for v in vowels:
        counter += line.count(v)
    print(counter, "", end="")