#
Name     : PyQt5
Version  : 5.9.2
Release  : 1
URL      : https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.9.2/PyQt5_gpl-5.9.2.tar.gz
Source0  : https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.9.2/PyQt5_gpl-5.9.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : qt-everywhere-opensource-src
BuildRequires : qt-everywhere-opensource-src-dev
BuildRequires : sip
BuildRequires : python3-dev
BuildRequires : mesa-dev


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
python3 configure.py --confirm-license

make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1515338975
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/share/sip/PyQt5
/usr/lib/python3.6/site-packages/PyQt5/
/usr/bin/pylupdate5
/usr/bin/pyrcc5
/usr/bin/pyuic5
/usr/plugins/PyQt5/libpyqt5qmlplugin.so
/usr/plugins/designer/libpyqt5.so
