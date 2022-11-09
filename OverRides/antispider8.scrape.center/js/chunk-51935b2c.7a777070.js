(window.webpackJsonp = window.webpackJsonp || []).push([["chunk-51935b2c"], {
    "5a19": function(t, a, e) {},
    "8c53": function(t, a, e) {
        "use strict";
        var s = e("f49a");
        e.n(s).a
    },
    ca9c: function(t, a, e) {
        "use strict";
        var s = e("5a19");
        e.n(s).a
    },
    d504: function(t, a, e) {
        "use strict";
        e.r(a);
        var s = e("7d92")
          , n = {
            name: "Index",
            components: {},
            data: function() {
                return {
                    loading: !1,
                    total: null,
                    page: parseInt(this.$route.params.page || 1),
                    limit: 10,
                    movies: null
                }
            },
            mounted: function() {
                this.onFetchData()
            },
            methods: {
                transfer: e("3e22").a,
                onPageChange: function(t) {
                    this.$router.push({
                        name: "indexPage",
                        params: {
                            page: t
                        }
                    }),
                    this.onFetchData()
                },
                onFetchData: function() {
                    var t = this;
                    this.loading = !0;
                    var a = (this.page - 1) * this.limit
                      , e = Object(s.a)(this.$store.state.url.index);
                    this.$axios.get(this.$store.state.url.index, {
                        params: {
                            limit: this.limit,
                            offset: a,
                            token: e
                        }
                    }).then((function(a) {
                        var e = a.data
                          , s = e.results
                          , n = e.count;
                        t.loading = !1,
                        t.movies = s,
                        t.total = n
                    }
                    ))
                }
            }
        }
          , i = (e("ca9c"),
        e("8c53"),
        e("2877"))
          , r = Object(i.a)(n, (function() {
            var t = this
              , a = t.$createElement
              , e = t._self._c || a;
            return e("div", {
                attrs: {
                    id: "index"
                }
            }, [e("el-row", {
                directives: [{
                    name: "loading",
                    rawName: "v-loading",
                    value: t.loading,
                    expression: "loading"
                }]
            }, [e("el-col", {
                attrs: {
                    span: 18,
                    offset: 3
                }
            }, t._l(t.movies, (function(a) {
                return e("el-card", {
                    key: a.name,
                    staticClass: "item m-t",
                    attrs: {
                        shadow: "hover"
                    }
                }, [e("el-row", [e("el-col", {
                    attrs: {
                        xs: 8,
                        sm: 6,
                        md: 4
                    }
                }, [e("router-link", {
                    attrs: {
                        to: {
                            name: "detail",
                            params: {
                                key: t.transfer(a.id)
                            }
                        }
                    }
                }, [e("img", {
                    staticClass: "cover",
                    attrs: {
                        src: a.cover
                    }
                })])], 1), e("el-col", {
                    staticClass: "p-h",
                    attrs: {
                        xs: 9,
                        sm: 13,
                        md: 16
                    }
                }, [e("router-link", {
                    staticClass: "name",
                    attrs: {
                        to: {
                            name: "detail",
                            params: {
                                key: t.transfer(a.id)
                            }
                        }
                    }
                }, [e("h2", {
                    staticClass: "m-b-sm"
                }, [t._v(t._s(a.name) + " - " + t._s(a.alias))])]), e("div", {
                    staticClass: "categories"
                }, t._l(a.categories, (function(a) {
                    return e("el-button", {
                        key: a,
                        staticClass: "category",
                        attrs: {
                            size: "mini",
                            type: "primary"
                        }
                    }, [t._v(t._s(a) + "\n              ")])
                }
                )), 1), e("div", {
                    staticClass: "m-v-sm info"
                }, [e("span", [t._v(t._s(a.regions.join("、")))]), e("span", [t._v(" / ")]), e("span", [t._v(t._s(a.minute) + " 分钟")])]), e("div", {
                    staticClass: "m-v-sm info"
                }, [e("span", [t._v(t._s(a.published_at) + " 上映")])])], 1), e("el-col", {
                    attrs: {
                        xs: 5,
                        sm: 5,
                        md: 4
                    }
                }, [e("p", {
                    staticClass: "score m-t-md m-b-n-sm"
                }, [t._v(t._s(a.score.toFixed(1)))]), e("p", [e("el-rate", {
                    attrs: {
                        value: a.score / 2,
                        disabled: "",
                        max: 5,
                        "text-color": "#ff9900"
                    }
                })], 1)])], 1)], 1)
            }
            )), 1)], 1), e("el-row", [e("el-col", {
                attrs: {
                    span: 10,
                    offset: 11
                }
            }, [e("div", {
                staticClass: "pagination m-v-lg"
            }, [e("el-pagination", {
                attrs: {
                    background: "",
                    "current-page": t.page,
                    "page-size": t.limit,
                    layout: "total, prev, pager, next",
                    total: t.total
                },
                on: {
                    "current-change": t.onPageChange,
                    "update:currentPage": function(a) {
                        t.page = a
                    },
                    "update:current-page": function(a) {
                        t.page = a
                    }
                }
            })], 1)])], 1)], 1)
        }
        ), [], !1, null, "709281a6", null);
        a.default = r.exports
    },
    f49a: function(t, a, e) {}
}]);
