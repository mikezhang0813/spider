var url = "https://user.qzone.qq.com/proxy/domain/photo.qzone.qq.com/fcgi-bin/fcg_list_album_v3";

//function getCookie(text){
//
//    return text
//}
cookie = "pgv_pvid=6165849197; tvfe_boss_uuid=0cccded8887f5980; pgv_pvi=1493414912; RK=/Xgs9JF3Xr; ptcz=437f029baf76ce174f1d3ff73d26a0e3b65f3d70c2fed3c00ec1fcda3d52d6a7; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=6; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s_hat_seed=1; uin=o0991256338; skey=@tzJ1Yw5Ro; p_uin=o0991256338; pt4_token=8ldwfPQT*D2zV4RWaDFb8ScuJjfMtjqlt2NY*yhNJhg_; p_skey=8hZylJassfQzfTmkji1jwW0kcDXbUF6YqOf-JbBXJ8c_; randomSeed=226115; pgv_info=ssid=s7680386045; rv2=808B23722C2E330B6B1B04F9884274B1D2411CE9A65B482266; property20=94A1A2B4EFAFFC344E6719986C3ACFCDF8D6728EFF03C535FE054E714FA5E7B8ACEF016C80880A68"
function token(e, t) {
            var o = ""
              , r = 5381;
            f = cookie.split(";");


            for(var i = 0;i<f.length;i++){
                if(f[i].substring(0,f[i].indexOf("=")).trim() == "skey"){
                            o = f[i].substring(f[i].indexOf("=")+1).trim()
                    }
                 }
            if (e) {
                var a = "user.qzone.qq.com";
                if (a.indexOf("qun.qq.com") > -1 || a.indexOf("qzone.qq.com") > -1 && a.indexOf("qun.qzone.qq.com") === -1) {
                    f = cookie.split(";");


                    for(var i = 0;i<f.length;i++){
                        if(f[i].substring(0,f[i].indexOf("=")).trim() == "p_skey"){
                            o = f[i].substring(f[i].indexOf("=")+1).trim()
                        }
                    }

                }
            }
            for (var c = 0, s = o.length; c < s; ++c) {
                r += (r << 5) + o.charAt(c).charCodeAt()
            }
            return r & 2147483647
}
function i(e, t, i) {
        if (typeof t != "undefined") {
            i = i || {
                domain: document.domain
            };
            if (t === null) {
                t = "";
                i.expires = -1
            }
            var o = "";
            if (i.expires && (typeof i.expires == "number" || i.expires.toUTCString)) {
                var r;
                if (typeof i.expires == "number") {
                    r = new Date;
                    r.setTime(r.getTime() + i.expires * 1e3)
                } else {
                    r = i.expires
                }
                o = "; expires=" + r.toUTCString()
            }
            var a = i.path ? "; path=" + i.path : "";
            var c = i.domain ? "; domain=" + i.domain : "";
            var s = i.secure ? "; secure" : "";
            document.cookie = [e, "=", encodeURIComponent(t), o, a, c, s].join("")
        } else {
            var u = null;
            var f = "gv_pvid=6165849197; tvfe_boss_uuid=0cccded8887f5980; pgv_pvi=1493414912; pgv_si=s4267051008; uin=o0991256338; skey=@JrVlKShrM; RK=/Xgs9JF3Xr; ptcz=437f029baf76ce174f1d3ff73d26a0e3b65f3d70c2fed3c00ec1fcda3d52d6a7; p_uin=o0991256338; Loading=Yes; qz_screen=1920x1080; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; pgv_info=ssid=s1604766405; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=6; pt4_token=hueGWV5IKopVQu53o65y*WsN6TnEP*TDWMkfzi5M4LA_; p_skey=lcP*T*lBK9guLIpoLHTCoxPDg5fJiDATYl8pkJnUJMY_; rv2=80992959E55CC90BA79A6AD7757883249FEE305BD6E5321E37; property20=D7229BA472BDAE80B80DEAC7382D8561AC3F55ADABB72843EE19BA1698E9960C8CFB00783F3A10C7; qzmusicplayer=qzone_player_532648630_1583410513133; __Q_w_s__QZN_TodoMsgCnt=1";
            try {
                f = top.document.cookie
            } catch (e) {}
            if (f && f != "") {
                var l = f.split(";");
                for (var p = 0; p < l.length; p++) {
                    var d = l[p].trim();
                    if (d.substring(0, e.length + 1) == e + "=") {
                        u = decodeURIComponent(d.substring(e.length + 1));
                        break
                    }
                }
            }
            return u
        }

    return i
    }
function t() {
            var e = String(Math.random().toFixed(16)).slice(-9).replace(/^0/, "9");
            return e}