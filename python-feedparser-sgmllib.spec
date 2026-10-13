%global module feedparser_sgmllib

Name:		python-feedparser-sgmllib
Version:	2.1.0
Release:	1
Summary:	sgmllib from Python 2.7 for feedparser
License:	PSF-2.0
Group:		Development/Python
URL:		https://github.com/python-syndication/feedparser-sgmllib
Source0:	https://files.pythonhosted.org/packages/source/f/feedparser-sgmllib/feedparser_sgmllib-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
feedparser-sgmllib is the Python 2.7 sgmllib module, kept so feedparser can
parse markup. feedparser 6.0.14 imports it as feedparser_sgmllib.

%files
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
