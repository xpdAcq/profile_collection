#from xpdan.pipelines.main import conf_main_pipeline
#from xpdan.pipelines.callback import MainCallback
#from shed.event_streams import istar
from bluesky.utils import install_qt_kicker
import shutil
import os
from pprint import pprint
from xpdsim import xpd_wavelength
from xpdan.vend.callbacks.zmq import Proxy, Publisher, RemoteDispatcher
import multiprocessing

'''
def start_proxy():
    Proxy(5567, 5568).start()

proxy_proc = multiprocessing.Process(target=start_proxy, daemon=True)
proxy_proc.start()
time.sleep(5)  # Give this plenty of time to start up.

'''
p = Publisher('127.0.0.1:5567', RE=xrun, prefix=b'raw')  # noqa

'''
def make_and_start_dispatcher(db):
    s = MainCallback(db, glbl['tiff_base'], calibration_md_folder='~/xpdUser/config_base')
    d = RemoteDispatcher('127.0.0.1:5568')
    install_qt_kicker(loop=d.loop)
    d.subscribe(s)
    print("REMOTE IS READY TO START")
    d.start()

dispatcher_proc = multiprocessing.Process(target=make_and_start_dispatcher,
                                              daemon=True, args=(db,))

dispatcher_proc.start()
'''
#time.sleep(5)  # As above, give this plenty of time to start.
#'''
# s = conf_main_pipeline(db, glbl['tiff_base'], vis=False, write_to_disk=True, calibration_md_folder='~/xpdUser/config_base')
#pt = xrun.subscribe(istar(s.emit))
#s = MainCallback(db, glbl['tiff_base'], calibration_md_folder='~/xpdUser/config_base')
#pt = xrun.subscribe(s)
# xrun.subscribe(lambda x, y: pprint(y))
install_qt_kicker(loop=xrun.loop)
# start a beamtime
PI_name = 'Billinge '
saf_num = 300000
wavelength = xpd_wavelength
experimenters = [('van der Banerjee', 'S0ham', 1),
                 ('Terban ', ' Max', 2)]
try:
    bt = _start_beamtime(PI_name, saf_num,
                         experimenters,
                         wavelength=wavelength)
except FileExistsError:
    pass
# spreadsheet
glbl['dk_window'] = 0.1
pytest_dir = rs_fn('xpdacq', 'tests/')
xlf = '300000_sample.xlsx'
src = os.path.join(pytest_dir, xlf)
shutil.copyfile(src, os.path.join(glbl_dict['import_dir'], xlf))
import_sample_info(saf_num, bt)
xrun.beamtime = bt
# xrun(0, 1, composition_string='Ni')
# run_calibration()
