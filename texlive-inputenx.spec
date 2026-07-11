%global tl_name inputenx
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.12
Release:	%{tl_revision}.1
Summary:	Enhanced input encoding handling
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/inputenx
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inputenx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inputenx.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inputenx.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package deals with input encodings. It provides a wider range of
input encodings using standard mappings, than does inputenc; it also
covers nearly all slots. In this way, it serves as more uptodate
replacement for package inputenc.

