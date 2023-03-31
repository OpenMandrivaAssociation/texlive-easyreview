Name:		texlive-easyreview
Version:	38352
Release:	2
Summary:	Package to provide a way to review (or perform editorial process) in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/easyreview
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easyreview.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easyreview.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easyreview.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The easyReview package provides a way to review (or perform
editorial process) in LaTeX. You can use the provided commands
to claim attention in different ways to part of the text, or
even to indicate that a text was added, needs to be removed,
needs to be replaced and add comments to the text.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/easyreview
%{_texmfdistdir}/tex/latex/easyreview
%doc %{_texmfdistdir}/doc/latex/easyreview

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
