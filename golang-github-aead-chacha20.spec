# Run tests in check section
%bcond_without check

%global goipath         github.com/aead/chacha20
%global commit          e2538746bfea853aaa589feb8ec46bd46ee78f86

%global common_description %{expand:
This package provides implementations of three ChaCha versions:

 - ChaCha20 with a 64 bit nonce (can en/decrypt up to 2^64 * 64 bytes for one 
 key-nonce combination)
 - ChaCha20 with a 96 bit nonce (can en/decrypt up to 2^32 * 64 bytes ~ 256 GB 
 for one key-nonce combination)
 - XChaCha20 with a 192 bit nonce (can en/decrypt up to 2^64 * 64 bytes 
 for one key-nonce combination)

Furthermore the chacha sub package implements ChaCha20/12 and ChaCha20/8. 
These versions use 12 or 8 rounds instead of 20. But it's recommended to use 
ChaCha20 (with 20 rounds) - it will be fast enough for almost all purposes.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        ChaCha20 and XChaCha20 stream ciphers
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
BuildRequires:  golang(golang.org/x/sys/cpu)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gite253874
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1.20180517gite253874
- First package for Fedora

