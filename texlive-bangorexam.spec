%global tl_name bangorexam
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6.0
Release:	%{tl_revision}.1
Summary:	Typeset an examination at Bangor University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bangorexam
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bangorexam.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bangorexam.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bangorexam.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows typesetting of Bangor University's exam style. It
currently supports a standard A/B choice, A-only compulsory and 'n' from
'm' exam styles. Marks are totalled and checked automatically.

