Summary:	X11 Window Manager - Windows 95/98 like environment
Summary(pl):	Mened¿er okienek X11 - ¶rodowisko podobne do Windows 95/98
Name:		qvwm
Version:	1.1.11
Release:	1
License:	LGPL
Group:		X11/Window Managers
Source0:	http://www.qvwm.org/archive/qvwm/%{name}-%{version}.tar.gz
Patch0:		http://www.qvwm.org/archive/qvwm/%{name}-%{version}-20010602.patch.gz
URL:		http://www.qvwm.org/
BuildRequires:	XFree86-devel
BuildRequires:	esound-devel >= 0.2.6
BuildRequires:	imlib-devel >= 1.8.2
BuildRequires:	libstdc++-devel
Requires:	fileutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Qvwm is a Windows 95/98/NT like window manager for X Window System. It
allows Windows 95/98/NT users to use X Window System without
hesitation and X Window System users to use Windows 95/98/NT without
hesitation.

%description -l pl
Qvwm jest mened¿erem okienek X11 wygl±daj±cym jak Windows 95/98/NT.
Pozwala on u¿ytkownikom 95/98/NT na wygodn± pracê w X Window jak i
u¿ytkownikom X Window na swobodn± pracê w Windows 95/98/NT.

%prep -q
%setup -q
%patch0 -p1

%build
%configure2_13 \
	--enable-rmtcmd \
	--enable-xsmp \
	--enable-ss \
	--without-alsa

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf doc/*.en

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/*
