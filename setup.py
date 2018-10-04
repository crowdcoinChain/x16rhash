from distutils.core import setup, Extension

xcoin_hash_module = Extension('x16_hash',
                               sources = ['xcoinmodule.c',
                                          'xcoin.c',
										  'sha3/blake.c',
										  'sha3/bmw.c',
										  'sha3/groestl.c',
										  'sha3/jh.c',
										  'sha3/keccak.c',
										  'sha3/skein.c',
										  'sha3/cubehash.c',
										  'sha3/echo.c',
										  'sha3/luffa.c',
										  'sha3/simd.c',
										  'sha3/shavite.c',
										  'sha3/sph_hamsi.c',
										  'sha3/sph_fugue.c',
										  'sha3/sph_shabal.c',
										  'sha3/sph_whirlpool.c',
										  'sha3/sph_sha512.c'
										  ],
                               include_dirs=['.', './sha3'])

setup (name = 'x16_hashs',
       version = '1.0',
       description = 'Bindings for proof of work used by Xcoin',
       ext_modules = [xcoin_hash_module])
