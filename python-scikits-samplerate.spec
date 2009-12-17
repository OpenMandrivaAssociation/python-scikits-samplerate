%define tarname	scikits.samplerate
%define name	python-scikits-samplerate
%define version	0.3.3
%define release	%mkrel 2

Summary:	Python wrapper for libsamplerate
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
Source1:	site.cfg
License:	BSD-like
Group:		Development/Python
Url:		http://www.ar.media.kyoto-u.ac.jp/members/david/softwares/pysamplerate/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-numpy >= 1.2.0, python-numpy-devel >= 1.2.0, libsamplerate-devel
BuildRequires:	python-setuptools
%py_requires -d
# Package is not noarch because code loads libs differently on x86_64

%description 
Samplerate is a Python module that permits one to perform high
quality resampling of audio signals using libsamplerate. The module
provides functionality similar to that of the resample function in
Matlab. It is intended to be used with numpy arrays.

%prep
%setup -q -n %{tarname}-%{version}
%__cp %SOURCE1 .

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=FILELIST

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%doc README Changelog
