Name:		texlive-inputenx
Version:	52986
Release:	2
Summary:	Enhanced input encoding handling
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/inputenx
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inputenx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inputenx.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inputenx.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package deals with input encodings. It provides a wider
range of input encodings using standard mappings, than does
inputenc; it also covers nearly all slots. In this way, it
serves as more uptodate replacement for package inputenc.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/inputenx
%{_texmfdistdir}/tex/latex/inputenx
%doc %{_texmfdistdir}/doc/latex/inputenx

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
