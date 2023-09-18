const Crypto = require("crypto")


l = {payload: 'LBc3V0I6ZGB6bXsxTCQnPRBuBhgbPj1fJDpwd2R1Tw==', sig: '49AF9D32DA6AA7E5B32214EC011FE0B7'};

let _keyStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';

payload = 'LBc3V0I6ZGB6bXsxTCQnPRBuBhgbPj1fJDpwd2R1Tw==';

let _p = 'W5D80NFZHAYB8EUI2T649RT2MNRMVE2O';

function _u_e(t) {
    if (null == t)
        return null;
    t = t.replace(/\r\n/g, "\n");
    for (var e = "", r = 0; r < t.length; r++) {
        var n = t.charCodeAt(r);
        n < 128 ? e += String.fromCharCode(n) : n > 127 && n < 2048 ? (e += String.fromCharCode(n >> 6 | 192),
            e += String.fromCharCode(63 & n | 128)) : (e += String.fromCharCode(n >> 12 | 224),
            e += String.fromCharCode(n >> 6 & 63 | 128),
            e += String.fromCharCode(63 & n | 128))
    }
    return e
}

function e2(t) {
    if (null == (t = _u_e(t)))
        return null;
    for (var e = "", r = 0; r < t.length; r++) {
        var n = _p.charCodeAt(r % _p.length);
        e += String.fromCharCode(t.charCodeAt(r) ^ n)
    }
    return e
}

function e1(t) {
    if (null == t)
        return null;
    for (var e, r, n, o, i, a, c, u = "", s = 0; s < t.length; )
        o = (e = t.charCodeAt(s++)) >> 2,
            i = (3 & e) << 4 | (r = t.charCodeAt(s++)) >> 4,
            a = (15 & r) << 2 | (n = t.charCodeAt(s++)) >> 6,
            c = 63 & n,
            isNaN(r) ? a = c = 64 : isNaN(n) && (c = 64),
            u = u + _keyStr.charAt(o) + _keyStr.charAt(i) + _keyStr.charAt(a) + _keyStr.charAt(c);
    return u
}

function sig(t) {
    var param = t + _p;
    return md5(param).toUpperCase()
}

function md5(text) {
    return Crypto.createHash('md5').update(text).digest('hex');
}

const f = e1(e2(JSON.stringify(payload)))
    , p = sig(f);

console.log(p);
