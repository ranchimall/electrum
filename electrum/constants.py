# -*- coding: utf-8 -*-
#
# Electrum - lightweight Bitcoin client
# Copyright (C) 2018 The Electrum developers
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import json


def read_json(filename, default):
    path = os.path.join(os.path.dirname(__file__), filename)
    try:
        with open(path, 'r') as f:
            r = json.loads(f.read())
    except:
        r = default
    return r


class AbstractNet:

    @classmethod
    def max_checkpoint(cls) -> int:
        return max(0, len(cls.CHECKPOINTS) * 2016 - 1)


class BitcoinMainnet(AbstractNet):

    TESTNET = False
    WIF_PREFIX = 0xa3
    ADDRTYPE_P2PKH = 35
    ADDRTYPE_P2SH = 94
    SEGWIT_HRP = "flo"
    GENESIS = "09c7781c9df90708e278c35d38ea5c9041d7ecfcdd1c56ba67274b7cff3e1cea"
    DEFAULT_PORTS = {'t': '50001', 's': '50002'}
    DEFAULT_SERVERS = read_json('servers.json', {})
    CHECKPOINTS = read_json('checkpoints.json', [])

    XPRV_HEADERS = {
        'standard':    0x01343c31,  # xprv
        'p2wpkh-p2sh': 0x049d7878,  # yprv
        'p2wsh-p2sh':  0x0295b005,  # Yprv
        'p2wpkh':      0x04b2430c,  # zprv
        'p2wsh':       0x02aa7a99,  # Zprv
    }
    XPUB_HEADERS = {
        'standard':    0x0134406b,  # xpub
        'p2wpkh-p2sh': 0x049d7cb2,  # ypub
        'p2wsh-p2sh':  0x0295b43f,  # Ypub
        'p2wpkh':      0x04b24746,  # zpub
        'p2wsh':       0x02aa7ed3,  # Zpub
    }
    BIP44_COIN_TYPE = 216
    # FLO Network constants
    fPowAllowMinDifficultyBlocks = False
    fPowNoRetargeting = False
    nRuleChangeActivationThreshold = 6048  # 75% of 8064
    nMinerConfirmationWindow = 8064
    # Difficulty adjustments
    nPowTargetSpacing = 40  # 40s block time
    # V1
    nTargetTimespan_Version1 = 60 * 60
    nInterval_Version1 = nTargetTimespan_Version1 / nPowTargetSpacing
    nMaxAdjustUp_Version1 = 75
    nMaxAdjustDown_Version1 = 300
    nAveragingInterval_Version1 = nInterval_Version1
    # V2
    nHeight_Difficulty_Version2 = 208440
    nInterval_Version2 = 15
    nMaxAdjustDown_Version2 = 300
    nMaxAdjustUp_Version2 = 75
    nAveragingInterval_Version2 = nInterval_Version2
    # V3
    nHeight_Difficulty_Version3 = 426000
    nInterval_Version3 = 1
    nMaxAdjustDown_Version3 = 3
    nMaxAdjustUp_Version3 = 2
    nAveragingInterval_Version3 = 6


class BitcoinTestnet(AbstractNet):

    TESTNET = True
    WIF_PREFIX = 0xef
    ADDRTYPE_P2PKH = 115
    ADDRTYPE_P2SH = 58
    SEGWIT_HRP = "tflo"
    GENESIS = "9b7bc86236c34b5e3a39367c036b7fe8807a966c22a7a1f0da2a198a27e03731"
    DEFAULT_PORTS = {'t': '51001', 's': '51002'}
    DEFAULT_SERVERS = read_json('servers_testnet.json', {})
    CHECKPOINTS = read_json('checkpoints_testnet.json', [])

    XPRV_HEADERS = {
        'standard':    0x01343c23,  # tprv
        'p2wpkh-p2sh': 0x044a4e28,  # uprv
        'p2wsh-p2sh':  0x024285b5,  # Uprv
        'p2wpkh':      0x045f18bc,  # vprv
        'p2wsh':       0x02575048,  # Vprv
    }
    XPUB_HEADERS = {
        'standard':    0x013440e2,  # tpub
        'p2wpkh-p2sh': 0x044a5262,  # upub
        'p2wsh-p2sh':  0x024289ef,  # Upub
        'p2wpkh':      0x045f1cf6,  # vpub
        'p2wsh':       0x02575483,  # Vpub
    }
    BIP44_COIN_TYPE = 1
    #Difficulty adjustments
    nPowTargetSpacing = 40 # 40 block time
    # V1
    nTargetTimespan_Version1 = 60 * 60
    nInterval_Version1 = nTargetTimespan_Version1 / nPowTargetSpacing;
    nMaxAdjustUp_Version1 = 75
    nMaxAdjustDown_Version1 = 300
    nAveragingInterval_Version1 = nInterval_Version1
    # V2
    nHeight_Difficulty_Version2 = 50000
    nInterval_Version2 = 15
    nMaxAdjustDown_Version2 = 300
    nMaxAdjustUp_Version2 = 75
    nAveragingInterval_Version2 = nInterval_Version2
    # V3
    nHeight_Difficulty_Version3 = 60000
    nInterval_Version3 = 1
    nMaxAdjustDown_Version3 = 3
    nMaxAdjustUp_Version3 = 2
    nAveragingInterval_Version3 = 6


class BitcoinRegtest(BitcoinTestnet):

    SEGWIT_HRP = "bcrt"
    GENESIS = "0f9188f13cb7b2c71f2a335e3a4fc328bf5beb436012afca590b1a11466e2206"
    DEFAULT_SERVERS = read_json('servers_regtest.json', {})
    CHECKPOINTS = []


class BitcoinSimnet(BitcoinTestnet):

    SEGWIT_HRP = "sb"
    GENESIS = "683e86bd5c6d110d91b94b97137ba6bfe02dbbdb8e3dff722a669b5d69d77af6"
    DEFAULT_SERVERS = read_json('servers_regtest.json', {})
    CHECKPOINTS = []


# don't import net directly, import the module instead (so that net is singleton)
net = BitcoinMainnet

def set_simnet():
    global net
    net = BitcoinSimnet

def set_mainnet():
    global net
    net = BitcoinMainnet


def set_testnet():
    global net
    net = BitcoinTestnet


def set_regtest():
    global net
    net = BitcoinRegtest
