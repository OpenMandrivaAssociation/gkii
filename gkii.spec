%define	oname	gkII

Summary:	Mandelbrot and Julia set image generator
Name:		gkii
Version:	0.4.6
Release:	%mkrel 1
License:	GPL
Group:		Graphics
Url:		http://www.jwm-art.net/gkII/
Source0:	http://www.jwm-art.net/gkII/%{oname}-src-%{version}.tar.bz2
BuildRequires:	libgtk+2-devel
BuildRequires:	libpng-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description 
It features unlimited image size, anti-aliasing, Mandelbrot/Julia mangling, 
autolayers with ramped bailout/perturbation, and controllable colour palette 
randomization, striping, scaling, and interpolation.

%prep
%setup -qn %{oname}-%{version}

%build

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}/gallery

install gkII %{buildroot}%{_bindir}/%{name}
install gallery/* %{buildroot}%{_datadir}/%{name}/gallery
%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES KEYS LICENSE README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}/gallery/*


