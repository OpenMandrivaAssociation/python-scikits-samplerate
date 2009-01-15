%define tarname	samplerate
%define name	python-scikits-samplerate
%define version	0.2
%define release	%mkrel 1

Summary:	Python wrapper for libsamplerate
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.lzma
Source1:	site.cfg
License:	BSD-like
Group:		Development/Python
Url:		http://www.ar.media.kyoto-u.ac.jp/members/david/softwares/pysamplerate/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	libsamplerate0
BuildRequires:	python-devel, python-numpy, libsamplerate-devel
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