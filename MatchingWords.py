#input
# nak ryc miq jyk jix byk jes los mat vec moh zip bop mof zaq les zis ruk zyt lah jyc bus zyc vyf def nyf gap zuq zaq dok dik mok jif vyp doq jyx dux nuc jyh jih gyq vex zit baq lyp git nes bof bap mas ros dek gik dyx vus roh ges vax duc zeh vyh zeh joc lih mof vuk myt nus ryh lis ges miq vyc des byh zip jet lip mup lyh dip res rec roh zok joh gek goq nep gyh lof gap boc lec nat gut geq dok jyf voq dyt mef buk zop ruq juk dot zyq nes rik las gas nuh luq myt lup gas nuh gos nas juk jas jup jic buf nyq mic not dik dof laf mif rof juc dys ret jes nif ryh mak giq rip lap nap vot gyx vot zuh nuq nec vep juf gyt ges bes dyq vox zep zax zut jik dux nat bux lyx ris bah buk met voq liq dyp nux vok jix deq zif zit dap nex meh doh zyt zix jiq jyk gip juk gyt mep jyf lat muk vos ziq lyp lep req ruh zyt vaq zis zup nyf vat lek lit diq dik mox ruk lyc mix dik jet nih zeh buf dus myf vox mat jiq jap gyh dip muq byh gux gut raq gih mis nyq jah but zih zot jeq dek nuh jyf lyx gef zic box jof gyc vok jek nak jyt rep jut met lut ryc vyx jos jep bys lax dac ros roq dus dyh doc dys lap dic naq jux gup noh veh byk bat mop let rox dus ryx lah rac mak giq baf reh joh moq bec jix mih buh lat jyf vit voq bes mup vuc zah zef vih end

words = [x for x in input().split()]
dict = {}

for word in words:
  if word in dict:
    dict[word] += 1
  else:
    dict[word] = 1

magic_words = []

for k in dict.keys():
  if dict[k] > 1:
    magic_words.append(k)

magic_words = sorted(magic_words)

print(" ".join(magic_words))