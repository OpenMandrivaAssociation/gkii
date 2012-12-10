%define	oname	gkII

Summary:	Mandelbrot and Julia set image generator
Name:		gkii
Version:	0.4.7
Release:	3
License:	GPL
Group:		Graphics
Url:		http://www.jwm-art.net/gkII/
Source0:	http://www.jwm-art.net/gkII/%{oname}-%{version}.tar.bz2
Patch0:		gkII-0.4.7-Makefile.patch
Patch1:		gkII-0.4.7-libpng15.patch
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libpng)

%description 
It features unlimited image size, anti-aliasing, Mandelbrot/Julia mangling, 
autolayers with ramped bailout/perturbation, and controllable colour palette 
randomization, striping, scaling, and interpolation.

%prep
%setup -qn %{oname}-%{version}
%patch0 -p1
%patch1 -p1

%build
%setup_compile_flags
pushd src
%make
popd

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}/gallery

install src/gkII %{buildroot}%{_bindir}/%{name}
install gallery/* %{buildroot}%{_datadir}/%{name}/gallery

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES KEYS LICENSE README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}/gallery

