#
# Conditional build:
%bcond_without	alsa	# without ALSA support
#
Summary:	X11 Window Manager - Windows 95/98 like environment
Summary(pl):	Zarz±dca okienek X11 - ¶rodowisko podobne do Windows 95/98
Name:		qvwm
Version:	1.1.12
Release:	4
License:	LGPL
Group:		X11/Window Managers
Source0:	ftp://ftp.qvwm.org/pub/qvwm/%{name}-%{version}.tar.gz
# Source0-md5:	688c44ca560e42315879f5b373d94a38
Source1:        %{name}-xsession.desktop
Patch0:		%{name}-am15.patch
Patch1:		%{name}-man_MANS.patch
Patch2:		%{name}-jp2ja.patch
URL:		http://www.qvwm.org/
BuildRequires:	XFree86-devel
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.6
BuildRequires:	imlib-devel >= 1.8.2
BuildRequires:	libstdc++-devel
Requires:	fileutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qvwm is a Windows 95/98/NT like window manager for X Window System. It
allows Windows 95/98/NT users to use X Window System without
hesitation and X Window System users to use Windows 95/98/NT without
hesitation.

%description -l pl
Qvwm jest zarz±dc± okienek X11 wygl±daj±cym jak Windows 95/98/NT.
Pozwala on u¿ytkownikom 95/98/NT na wygodn± pracê w X Window jak i
u¿ytkownikom X Window na swobodn± pracê w Windows 95/98/NT.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

for a in `find -type f -name "*jp"`
	do mv $a `echo $a | sed -e 's/jp$/ja/'`
done
mv man/jp man/ja

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"
%configure \
	%{!?with_alsa:--without-alsa} \
	--enable-rmtcmd \
	--enable-xsmp \
	--enable-ss

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/xsessions
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.en
%lang(fr) %doc doc/*.fr
%lang(ja) %doc doc/*.ja
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man?/*
%lang(fr) %{_mandir}/fr/man?/*
%lang(ja) %{_mandir}/ja/man?/*
