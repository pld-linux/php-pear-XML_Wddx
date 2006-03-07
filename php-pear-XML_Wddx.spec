%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	Wddx
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Wddx pretty serializer and deserializer
Summary(pl):	%{_pearname} - przyzwoity serializer i deserializer Wddx
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6512882461a3b9da49382be1baf1f1e3
URL:		http://pear.php.net/package/XML_Wddx/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-XML_Parser >= 1.0
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
- zastêpuje rozszerzenie XML_Wddx (je¶li nie jest wbudowane)
- tworzy edytowalny plik wddx (z wciêciami itp.) i u¿ywa CDATA zamiast
  znaczników znakowych

Ten pakiet zawiera 2 statyczne metody:
- XML_Wddx:serialize($value)
- XML_Wddx:deserialize($value)

i powinien byæ w 90% kompatybilny z wddx_deserialize(), a deserializer
bêdzie u¿ywa³ wddx_deserialize je¶li zosta³o wbudowane.

Aktualnie nie ma obs³ugi dla zbiorów rekordów w wersji PHP
deserializera.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
