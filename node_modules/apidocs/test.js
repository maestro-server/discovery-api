/* istanbul instrument in package apidoc */
/*jslint
    bitwise: true,
    browser: true,
    maxerr: 8,
    maxlen: 96,
    node: true,
    nomen: true,
    regexp: true,
    stupid: true
*/
(function () {
    'use strict';
    var local;



    // run node js-env code - pre-init
    (function () {
        // init local
        local = {};
        // init modeJs
        local.modeJs = 'node';
        // init global
        local.global = global;
        switch (local.modeJs) {
        // re-init local from example.js
        case 'node':
            local = (local.global.utility2_rollup || require('utility2'))
                .requireExampleJsFromReadme();
            local.global.local = local;
            break;
        }
    }());
    switch (local.modeJs) {



    // run node js-env code - function
    case 'node':
        local.testCase_apidocCreate_default = function (options, onError) {
        /*
         * this function will test apidocCreate's default handling-behavior-behavior
         */
            options = {
                // test dir-custom handling-behavior
                dir: local.utility2.__dirname
            };
            local.apidocCreate(options);
            options = {
                // test libFilelist-custom handling-behavior
                libFileList: ['lib.apidoc.js', 'package.json'],
                // test invalid module-name handling-behavior
                moduleDict: { 'invalid syntax': {} },
                // test packageJson default handling-behavior
                packageJson: {},
                // test markdown-template handling-behavior
                template: local.templateApidocMd
            };
            local.apidocCreate(options);
            local.testMock([
                // test libFileList-error handling-behavior
                [local.fs, { readdirSync: function () {
                    return ['undefined'];
                } }]
            ], function (onError) {
                options = {};
                local.apidocCreate(options);
                onError();
            }, onError);
        };

        local.testCase_buildApidoc_default = function (options, onError) {
        /*
         * this function will test buildApidoc's default handling-behavior-behavior
         */
            options = {};
            local.buildApidoc(options, onError);
        };

        local.testCase_buildApp_default = function (options, onError) {
        /*
         * this function will test buildApp's default handling-behavior-behavior
         */
            local.testCase_buildReadme_default(options, local.onErrorDefault);
            onError();
        };

        local.testCase_buildReadme_default = function (options, onError) {
        /*
         * this function will test buildReadme's default handling-behavior-behavior
         */
            options = {};
            options.customize = function () {
                // search-and-replace - customize readmeTo
                [
                    // customize demo
                    (/\n\[!\[package-listing\][\S\s]*?\n# documentation\n/),
                    // customize test-server
                    (/\n\| git-branch : \|[\S\s]*?\n\| test-report : \|/),
                    // customize quickstart
                    (/\n# quickstart[\S\s]*?\n# package.json\n/)
                ].forEach(function (rgx) {
                    options.readmeFrom.replace(rgx, function (match0) {
                        options.readmeTo = options.readmeTo.replace(rgx, match0);
                    });
                });
            };
            local.buildReadme(options, onError);
        };
        break;
    }
    switch (local.modeJs) {



    // run node js-env code - post-init
    case 'node':
        // run test-server
        local.testRunServer(local);
        break;
    }
}());
