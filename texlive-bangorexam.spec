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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows typesetting of Bangor University's exam style. It
currently supports a standard A/B choice, A-only compulsory and 'n' from
'm' exam styles. Marks are totalled and checked automatically.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bangorexam
%dir %{_datadir}/texmf-dist/source/latex/bangorexam
%dir %{_datadir}/texmf-dist/tex/latex/bangorexam
%doc %{_datadir}/texmf-dist/doc/latex/bangorexam/README.txt
%doc %{_datadir}/texmf-dist/doc/latex/bangorexam/bangorexam.pdf
%doc %{_datadir}/texmf-dist/source/latex/bangorexam/bangorexam.dtx
%doc %{_datadir}/texmf-dist/source/latex/bangorexam/bangorexam.ins
%{_datadir}/texmf-dist/tex/latex/bangorexam/bangorexam.cls
