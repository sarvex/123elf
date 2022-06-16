Name:           lotus123r3
Version:        1.0.0rc1
Release:        1%{?dist}
Summary:        Create, modify, and process financial or scientific models.
License:        Abandonware
URL:            https://github.com/taviso/123elf
Source0:        https://github.com/taviso/123elf/archive/refs/tags/v1.0.0-rc1.tar.gz
Source1:        https://archive.org/compress/123-unix/formats=ISO%20IMAGE&file=/123-unix.zip
Requires:       ncurses-libs(x86-32) glibc(x86-32)

%description
The 123 command is a spreadsheet application for UNIX-based systems that can
be used in interactive mode to create and modify financial and  scientific
models.

%prep
%setup -q -n 123elf-1.0.0-rc1 -a 1

%build
./extract.sh
./binutils.sh
make

%install
make install prefix=%{buildroot}/%{_prefix}

%files
%{_prefix}/share/lotus
%{_prefix}/share/man/man1/123.1.gz
%{_prefix}/bin/123

%changelog
* Thu Jun 16 2022 Tavis Ormandy <taviso@gmail.com>
- Initial Version