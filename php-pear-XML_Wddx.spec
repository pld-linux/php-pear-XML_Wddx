%include	/usr/lib/rpm/macros.php
%define         _class          XML
%define         _subclass       Wddx
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Wddx pretty serializer and deserializer
#Summary(pl):	%{_pearname} -
Name:		php-pear-%{_pearname}
Version:	0.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e2f443fbb0bbb2d9df6cb4a9d139150d
URL:		http://pear.php.net/package/XML_Wddx/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML_Wddx does 2 things:
- a drop in replacement for the XML_Wddx extension (if it's not built in)
- produce an editable wddx file (with indenting etc.) and uses CDATA,
  rather than char tags

This package contains 2 static method:
- XML_Wddx:serialize($value)
- XML_Wddx:deserialize($value)

And should be 90% compatible with wddx_deserialize(), and the
deserializer will use wddx_deserialize if it is built in.

No support for recordsets is available at present in the PHP version
of the deserializer.

This class has in PEAR status: %{_status}.

#%description -l pl
#...
#
#Ta klasa ma w PEAR status: %{_status}.

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
