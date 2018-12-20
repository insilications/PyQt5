#
Name     : PyQt5
Version  : 5.9.2
Release  : 6
URL      : https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.9.2/PyQt5_gpl-5.9.2.tar.gz
Source0  : https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.9.2/PyQt5_gpl-5.9.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : sip sip-dev
BuildRequires : python3-dev
BuildRequires : mesa-dev
BuildRequires : buildreq-kde
BuildRequires : qscintilla qscintilla-dev

BuildRequires : qtbase-dev qtxmlpatterns-dev qtcanvas3d qtcharts-dev qtconnectivity-dev qtdeclarative-dev qtgraphicaleffects qtimageformats-dev qtlocation-dev
BuildRequires : qtmultimedia-dev qtquickcontrols qtquickcontrols2 qtscript-dev qtscxml-dev qtsensors-dev qtserialbus-dev qtserialport-dev
BuildRequires : qtsvg-dev qttools-dev qttranslations qtvirtualkeyboard-dev qtwebchannel-dev qtwebsockets-dev qtx11extras-dev qtxmlpatterns-dev


%description
PyQt5 - Python Bindings for the Qt v5 Toolkit
INTRODUCTION
These are the Python bindings for Qt v5.  Python v2.6 or later is required.
You must also have the SIP Python bindings generator installed.  PyQt4 is also
available which supports earlier versions of Python, and Qt v4 and the
compatible subset of Qt v5.

%prep
%setup -q -n PyQt5_gpl-5.9.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1515338975
python3 configure.py --confirm-license --verbose --disable=QtTest

make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1515338975
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/share/sip/PyQt5
/usr/lib/python3.*/site-packages/PyQt5/
/usr/bin/pylupdate5
/usr/bin/pyrcc5
/usr/bin/pyuic5
/usr/share/qt5/qsci/api/python/PyQt5.api