%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	Wddx
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Wddx pretty serializer and deserializer
Summary(pl):	%{_pearname} - przyzwoity serializer i deserializer Wddx
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	37e6c3b0a2fe513a060c7c41b45775ec
URL:		http://pear.php.net/package/XML_Wddx/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML_Wddx does 2 things:
- a drop in replacement for the XML_Wddx extension (if it's not built
  in)
- produce an editable wddx file (with indenting etc.) and uses CDATA,
  rather than char tags

This package contains 2 static method:
- XML_Wddx:serialize($value)
- XML_Wddx:deserialize($value)

And should be 90% compatible with wddx_deserialize(), and the
deserializer will use wddx_deserialize if it is built in.

No support for recordsets is available at present in the PHP version
of the deserializer.

In PEAR status of this package is: %{_status}.

%description -l pl
XML_Wddx robi dwie rzeczy:
- zast�puje rozszerzenie XML_Wddx (je�li nie jest wbudowane)
- tworzy edytowalny plik wddx (z wci�ciami itp.) i u�ywa CDATA zamiast
  znacznik�w znakowych

Ten pakiet zawiera 2 statyczne metody:
- XML_Wddx:serialize($value)
- XML_Wddx:deserialize($value)

i powinien by� w 90% kompatybilny z wddx_deserialize(), a deserializer
b�dzie u�ywa� wddx_deserialize je�li zosta�o wbudowane.

Aktualnie nie ma obs�ugi dla zbior�w rekord�w w wersji PHP
deserializera.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
