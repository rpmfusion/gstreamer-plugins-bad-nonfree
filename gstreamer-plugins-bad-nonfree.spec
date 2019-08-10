%define majorminor   0.10

Summary:        Non Free GStreamer streaming media framework "bad" plug-ins
Name:           gstreamer-plugins-bad-nonfree
Version:        0.10.23
Release:        10%{?dist}
License:        LGPLv2+
Group:          Applications/Multimedia
URL:            http://gstreamer.freedesktop.org/
Source:         http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.bz2
BuildRequires:  gstreamer-devel gstreamer-plugins-base-devel
BuildRequires:  faac-devel liboil-devel
BuildRequires:  check gettext-devel gcc

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that depend upon non-free libraries.


%prep
%setup -q -n gst-plugins-bad-%{version}


%build
%configure \
    --with-package-name="gst-plugins-bad rpmfusion rpm" \
    --with-package-origin="http://rpmfusion.org/" \
    --enable-debug --disable-static
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
pushd ext/faac
make %{?_smp_mflags} V=2
popd


%install
pushd ext/faac
make install V=2 DESTDIR=$RPM_BUILD_ROOT
popd
rm $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgst*.la


%files
%doc AUTHORS COPYING.LIB README
%{_libdir}/gstreamer-%{majorminor}/libgstfaac.so


%changelog
* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.10.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.10.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.10.23-8
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 0.10.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.10.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.10.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.10.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.10.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Mar  2 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 0.10.23-2
- Drop no longer needed PyXML BuildRequires (rf#2572)

* Sat Nov 10 2012 Hans de Goede <j.w.r.degoede@gmail.com> - 0.10.23-1
- New upstream release 0.10.23 (rf#2511)
- Drop amrwbenc plugin, use voamrwbenc from -bad (freeworld) instead

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.10.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 27 2011 Hans de Goede <j.w.r.degoede@gmail.com> - 0.10.22-2
- Rebuild for Fedora 16

* Tue May 17 2011 Hans de Goede <j.w.r.degoede@gmail.com> - 0.10.22-1
- New upstream release 0.10.22

* Thu Apr 21 2011 Hans de Goede <j.w.r.degoede@gmail.com> - 0.10.21-2
- Rebuild for proper package kit magic provides (rhbz#695730)

* Fri Jan 28 2011 Hans de Goede <j.w.r.degoede@hhs.nl> 0.10.21-1
- New upstream release 0.10.21

* Sun Mar 14 2010 Hans de Goede <j.w.r.degoede@hhs.nl> 0.10.18-1
- New upstream release 0.10.18

* Tue Jan  5 2010 Hans de Goede <j.w.r.degoede@hhs.nl> 0.10.17-2
- Various small specfile fixes from review (rf1015)

* Sat Dec 19 2009 Hans de Goede <j.w.r.degoede@hhs.nl> 0.10.17-1
- Initial RPM Fusion package
