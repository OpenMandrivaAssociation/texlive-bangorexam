Name:		texlive-bangorexam
Version:	46626
Release:	2
Summary:	Typeset an examination at Bangor University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bangorexam
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bangorexam.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bangorexam.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bangorexam.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows typesetting of Bangor Univesity's exam
style. It currently supports a standard A/B choice, A-only
compulsory and 'n' from 'm' exam styles. Marks are totalled and
checked automatically.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/bangorexam
%{_texmfdistdir}/tex/latex/bangorexam
%doc %{_texmfdistdir}/doc/latex/bangorexam

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
