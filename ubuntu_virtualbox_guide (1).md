# 🐧 Ubuntu VirtualBox Installation Guide – Real World Troubleshooting

[![OS](https://img.shields.io/badge/Host%20OS-Windows%2011-blue)]()
[![VirtualBox](https://img.shields.io/badge/VirtualBox-7.x-orange)]()
[![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04%20LTS-red)]()

> A honest documentation of my Ubuntu installation journey with VirtualBox, including all the things that went wrong and how I fixed them. If you're struggling with similar issues, this guide might save you some headaches! 😅

## 📋 Table of Contents

- [System Specifications](#-system-specifications)
- [Initial Setup](#️-initial-setup)
- [Common Problems & Solutions](#-common-problems--solutions)
  - [Ubuntu Keeps Asking to Install Again](#problem-1-ubuntu-kept-asking-me-to-install-again)
  - [Guest Additions Installation Issues](#problem-2-guest-additions-nightmare)
  - [Moving VM to Different Drive](#moving-ubuntu-vm-from-c-to-d-drive)
- [What Actually Worked](#-what-eventually-worked-for-me)
- [Lessons Learned](#-what-ill-do-next-time)
- [TL;DR Quick Fixes](#-tldr-quick-fixes)

---

## 💻 System Specifications

- **Host OS**: Windows 11
- **VirtualBox Version**: 7.0.x (Latest)
- **Ubuntu Version**: 22.04 LTS
- **RAM Allocated**: 4 GB
- **Storage**: 25 GB VDI
- **Disk Setup**: Only selected **hard disk** (unchecked all other storage options)

---

## ⚙️ Initial Setup

Basic VM configuration that I started with:

```
Memory: 4096 MB
Storage: 25 GB (VDI, Dynamically allocated)
Display: 128 MB video memory
Audio: Disabled (for performance)
Network: NAT
```

---

## 🔧 Common Problems & Solutions

### Problem #1: Ubuntu Kept Asking Me to Install Again

**What happened?**  
Every time I booted into Ubuntu, it would ask me to install it again like nothing ever happened 😩

**What I tried:**
- ✅ Changed the **boot order** so that the hard disk came first
- ✅ Switched the disk from ISO to "normal" after installation
- ✅ Tried enabling **floppy disk** in boot order (didn't help but worth trying)
- ❌ Removed duplicate Ubuntu entries in boot menu (this broke everything)

**Solution:**
1. **Remove the ISO after installation**: Settings > Storage > Remove Ubuntu ISO
2. **Fix boot order**: Settings > System > Boot Order > Hard Disk first
3. **Don't delete boot entries** unless you know what you're doing

---

### Problem #2: Guest Additions Nightmare

**What happened?**  
Tried installing Guest Additions from VirtualBox menu (`Devices > Insert Guest Additions CD image`) but got:

```bash
Could not mount the media/drive 'VBoxGuestAdditions.iso' (VERR_PDM_MEDIA_LOCKED)
```

**What I tried (and failed):**

```bash
# This got stuck at the second line
sudo apt update
sudo apt install build-essential dkms linux-headers-$(uname -r)
sudo apt install gcc make perl
```

```bash
# This froze Ubuntu at 47% during "Unboxing VirtualBox"
sudo apt update
sudo apt install virtualbox-guest-additions-iso virtualbox-guest-utils
sudo reboot
```

**What actually worked:**
- Gave up on Guest Additions 🙃
- Manually adjusted resolution: **Settings > Display > Resolution** in Ubuntu
- Not perfect, but functional enough

**Alternative solution to try:**
```bash
# If you want to attempt Guest Additions again
sudo apt update && sudo apt upgrade -y
sudo apt install build-essential dkms linux-headers-generic
# Then insert Guest Additions CD and run autorun.sh
```

---

### Moving Ubuntu VM from C: to D: Drive

**Problem:**  
Ran out of space on C: drive (literally 0 bytes), got I/O cache errors:
```
The I/O cache encountered an error while updating data in medium "ahci-0-0" (rc=VERR_DISK_FULL)
```

**Solution Steps:**
1. **Move VM folder**: Cut entire VM folder from `C:\Users\[Username]\VirtualBox VMs\Ubuntu` to `D:\VirtualBox VMs\Ubuntu`
2. **Handle saved state issues**: Delete `.sav` files if VM was in saved state
3. **Force quit VirtualBox** via Task Manager if it freezes
4. **Remove broken VM entry**: Machine > Remove (keep files)
5. **Re-add VM**: Machine > Add > Select `.vbox` file from new location
6. **Update storage paths**: Settings > Storage > Point to D: drive paths
7. **Set new default folder**: File > Preferences > General > Default Machine Folder → `D:\VirtualBox VMs`
8. **Create snapshot**: Take snapshot after successful move

---

## ✅ What Eventually Worked for Me

Final working configuration:
- Manual resolution adjustment in Ubuntu settings
- Storage set to "normal" (not ISO)
- Boot order: Hard disk first
- ISO removed after installation
- VM moved to D: drive with proper path updates

---

## 🔮 What I'll Do Next Time

- Try **Ubuntu Minimal install** to save resources
- **Take snapshots** immediately after successful install
- Consider **VMware Player** as alternative
- **Allocate more disk space** initially (30-40 GB)
- **Enable hardware acceleration** if available

---

## ⚡ TL;DR Quick Fixes

| Problem | Quick Solution |
|---------|----------------|
| Ubuntu keeps asking to install | Remove ISO, fix boot order |
| Guest Additions won't install | Skip it, use manual resolution |
| VM running out of space | Move to different drive, update paths |
| VM won't boot after changes | Check storage paths, remove saved states |
| Poor performance | Allocate more RAM, enable hardware acceleration |

---

## 🏷️ Tags

`VirtualBox` `Ubuntu` `Windows-11` `Virtualization` `Guest-Additions` `Troubleshooting` `Linux` `VM-Setup`

---

## 🤝 Contributing

Found a better solution or ran into different issues? Feel free to:
- Open an issue to discuss problems
- Submit a PR with additional solutions
- Share your own troubleshooting experiences

---

## ⚠️ Disclaimer

This guide reflects my personal experience with VirtualBox and Ubuntu. Your mileage may vary depending on your system configuration, VirtualBox version, and Ubuntu version. Always backup your VMs before making major changes!