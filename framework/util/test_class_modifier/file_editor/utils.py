def log_method_text():
    return ['',
            '\t//Added to trace test by exception using annotation',
            '\tpublic static void logException(Exception e){',
            '\t\t// do nothing',
            '\t}']


def get_throws_exception():
    return ['{ throws Exception']


def get_try_method():
    return ['\t\ttry {']


def get_catch_block():
    return ['} catch (Exception e) {',
            'logException(e);',
            'throw e;',
            '}']
