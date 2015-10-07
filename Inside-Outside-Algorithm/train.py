__author__ = 'zhouyang'

from CFG import CFG
from PCFG_EM import PCFG_EM
import os
def train(cfg_file,train_file,iter_num=20):
    cfg = CFG(cfg_file=cfg_file)
    pcfg = PCFG_EM(train_file=train_file,CFG=cfg)
    (name,ext) = os.path.splitext(train_file)
    state = pcfg.EM(iter_num=iter_num)
    with open(name+'.pcfg','w') as f:
        for (A,w) in cfg.unary_rules:
            f.writelines(A+'->'+w+' '+str(state.get((A,w)))+'\n')

        for (A,B,C) in cfg.binary_rules:
            f.writelines(A+'->'+B+' '+C+' '+str(state.get((A,B,C)))+'\n')
if __name__ == '__main__':
    #train('test/emile.cfg','test/emile.train')
    #train('test/test2.cfg','test/test2.train')
    #train('test/test3.cfg','test/test3.train')
    #train('test/test4.cfg','test/test4.train')
    #train('test/test5.cfg','test/test5.train')
    train('test/test1.cfg','test/test1.train')



