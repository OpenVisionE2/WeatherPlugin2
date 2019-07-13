from distutils.core import setup
import setup_translate

pkg = 'Extensions.WeatherPlugin2'
setup (name = 'enigma2-plugin-extensions-WeatherPlugin2',
       version = '2.1',
       description = 'Plugin to Weather.',
       packages = [pkg],
       package_dir = {pkg: 'usr'},
       package_data = {pkg: ['plugin.png', '*/*.png', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass = setup_translate.cmdclass, # for translation
      )
