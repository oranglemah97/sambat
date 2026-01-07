#!/usr/bin/env python3
"""
Auto Patcher untuk Bot SheerID
Jalankan: python auto_patcher.py
"""

def patch_bot_file():
    print("🔧 Auto Patcher Bot SheerID")
    print("="*70)

    try:
        # Baca file asli
        with open('paste.txt', 'r', encoding='utf-8') as f:
            code = f.read()

        print("✅ File paste.txt berhasil dibaca")
        print(f"📏 Ukuran: {len(code)} karakter")

        # PERBAIKAN #1: Simpan link lengkap
        old_1 = """                        await context.bot.send_message(
                            chat_id=chat_id,
                            text=(
                                "🔧 *Link tidak lengkap di email!*\\n\\n"
                                f"✅ emailToken ditemukan: `{email_token}`\\n"
                                "🔗 Building complete verification link...\\n\\n"
                                f"`{verification_link[:80]}...`"
                            ),
                            parse_mode="Markdown"
                        )"""

        new_1 = """                        # 🔥 PERBAIKAN #1: Simpan link lengkap ke storage
                        email_data["email_token"] = email_token
                        email_data["complete_verification_link"] = verification_link
                        temp_email_storage[user_id] = email_data

                        await context.bot.send_message(
                            chat_id=chat_id,
                            text=(
                                "🔧 *Link tidak lengkap di email!*\\n\\n"
                                f"✅ emailToken ditemukan: `{email_token}`\\n"
                                "🔗 Building complete verification link...\\n\\n"
                                f"`{verification_link[:80]}...`"
                            ),
                            parse_mode="Markdown"
                        )"""

        if old_1 in code:
            code = code.replace(old_1, new_1, 1)
            print("✅ Perbaikan #1: Simpan link lengkap - DONE")
        else:
            print("⚠️ Perbaikan #1: Pattern tidak ditemukan")

        # PERBAIKAN #2: Timeout notification
        old_2 = """    if check_count >= 30:
        await context.bot.send_message(
            chat_id=chat_id,
            text=(
                "⏰ *Email monitoring timeout*\\n\\n"
                "Tidak ada email verifikasi masuk dalam 5 menit.\\n"
                f"📧 Email: `{email_data.get('email')}`\\n\\n"
                "❌ *Verification FAILED*\\n\\n"
                "Kemungkinan:\\n"
                "• Data tidak valid\\n"
                "• SheerID butuh document upload\\n"
                "• Email belum dikirim\\n\\n"
                "Coba lagi dengan /start"
            ),
            parse_mode="Markdown"
        )
        await delete_email_inbox(email_data.get("email"))
        job.schedule_removal()
        temp_email_storage.pop(user_id, None)
        return"""

        new_2 = """    if check_count >= 30:
        # 🔥 PERBAIKAN #2: Ambil link lengkap dari storage
        complete_link = email_data.get("complete_verification_link", "")
        email_address = email_data.get("email", "N/A")

        timeout_text = (
            "⏰ *Email monitoring timeout*\\n\\n"
            "Tidak ada email verifikasi masuk dalam 5 menit.\\n"
            f"📧 Email: `{email_address}`\\n\\n"
            "❌ *Verification TIMEOUT*\\n\\n"
        )

        # Tambahkan link jika ada
        if complete_link:
            timeout_text += (
                "🔗 *Link verifikasi lengkap:*\\n"
                f"`{complete_link}`\\n\\n"
                "💡 *Coba manual:*\\n"
                "1. Klik link di atas\\n"
                "2. Atau cek inbox: "
                f"https://bot-emails.pilarjalar.workers.dev/emails/{email_address}\\n\\n"
            )
        else:
            timeout_text += (
                "⚠️ Email belum masuk atau link belum tersedia.\\n\\n"
                "💡 *Cara manual:*\\n"
                "1. Cek inbox email di browser\\n"
                f"   https://bot-emails.pilarjalar.workers.dev/emails/{email_address}\\n"
                "2. Tunggu email dari SheerID\\n"
                "3. Klik link di email\\n\\n"
            )

        timeout_text += "Ketik /start untuk mencoba lagi."

        await context.bot.send_message(
            chat_id=chat_id,
            text=timeout_text,
            parse_mode="Markdown"
        )
        await delete_email_inbox(email_address)
        job.schedule_removal()
        temp_email_storage.pop(user_id, None)
        return"""

        if old_2 in code:
            code = code.replace(old_2, new_2, 1)
            print("✅ Perbaikan #2: Timeout notification - DONE")
        else:
            print("⚠️ Perbaikan #2: Pattern tidak ditemukan")

        # PERBAIKAN #3: NOT APPROVED
        old_3 = """                        elif verification_status == "not_approved":
                            await context.bot.send_message(
                                chat_id=chat_id,
                                text=(
                                    "❌ *VERIFICATION NOT APPROVED*\\n\\n"
                                    "⚠️ *Status: NOT APPROVED / REJECTED*\\n\\n"
                                    f"📧 Email: `{email}`\\n"
                                    f"🎯 SheerID Status: `{sheerid_status}`\\n"
                                    f"📊 HTTP Status: `{click_result.get('status_code')}`\\n"
                                    f"💬 Message: {status_message}\\n\\n"
                                    "📋 *Alasan kemungkinan:*\\n"
                                    "• Data tidak cocok dengan database SheerID\\n"
                                    "• Informasi teacher tidak valid\\n"
                                    "• School tidak match\\n\\n"
                                    "💡 *Saran:*\\n"
                                    "• Cek kembali data yang diinput\\n"
                                    "• Gunakan data teacher yang valid\\n"
                                    "• Coba dengan data berbeda\\n\\n"
                                    "Ketik /start untuk mencoba lagi."
                                ),
                                parse_mode="Markdown"
                            )

                            await send_log(
                                f"❌ VERIFICATION NOT APPROVED ({BOT_NAME})\\n\\n"
                                f"User ID: {user_id}\\n"
                                f"Email: {email}\\n"
                                f"Status: NOT APPROVED\\n"
                                f"SheerID: {sheerid_status}"
                            )"""

        new_3 = """                        elif verification_status == "not_approved":
                            # 🔥 PERBAIKAN #3: Ambil link lengkap
                            complete_link = email_data.get("complete_verification_link", verification_link)

                            await context.bot.send_message(
                                chat_id=chat_id,
                                text=(
                                    "❌ *VERIFICATION NOT APPROVED*\\n\\n"
                                    "⚠️ *Status: NOT APPROVED / REJECTED*\\n\\n"
                                    f"📧 Email: `{email}`\\n"
                                    f"🎯 SheerID Status: `{sheerid_status}`\\n"
                                    f"📊 HTTP Status: `{click_result.get('status_code')}`\\n"
                                    f"💬 Message: {status_message}\\n\\n"
                                    "🔗 *Link verifikasi lengkap:*\\n"
                                    f"`{complete_link}`\\n\\n"
                                    "📋 *Alasan kemungkinan:*\\n"
                                    "• Data tidak cocok dengan database SheerID\\n"
                                    "• Informasi teacher tidak valid\\n"
                                    "• School tidak match\\n\\n"
                                    "💡 *Coba manual:*\\n"
                                    "1. Klik link di atas di browser\\n"
                                    "2. Verifikasi dengan data yang benar\\n"
                                    "3. Atau coba dengan data teacher lain\\n\\n"
                                    "Ketik /start untuk mencoba lagi."
                                ),
                                parse_mode="Markdown"
                            )

                            await send_log(
                                f"❌ VERIFICATION NOT APPROVED ({BOT_NAME})\\n\\n"
                                f"User ID: {user_id}\\n"
                                f"Email: {email}\\n"
                                f"Status: NOT APPROVED\\n"
                                f"SheerID: {sheerid_status}\\n"
                                f"Link: {complete_link}"
                            )"""

        if old_3 in code:
            code = code.replace(old_3, new_3, 1)
            print("✅ Perbaikan #3: NOT APPROVED notification - DONE")
        else:
            print("⚠️ Perbaikan #3: Pattern tidak ditemukan")

        # PERBAIKAN #4: UNKNOWN
        old_4 = """                        else:
                            await context.bot.send_message(
                                chat_id=chat_id,
                                text=(
                                    "⚠️ *VERIFICATION STATUS UNCLEAR*\\n\\n"
                                    "🔄 *Status: UNKNOWN / AMBIGUOUS*\\n\\n"
                                    f"📧 Email: `{email}`\\n"
                                    f"🎯 SheerID Status: `{sheerid_status}`\\n"
                                    f"📊 HTTP Status: `{click_result.get('status_code')}`\\n\\n"
                                    "💡 Akses link ini di browser untuk cek status:\\n"
                                    f"`{click_result.get('final_url', 'N/A')}`\\n\\n"
                                    "Response preview:\\n"
                                    f"`{click_result.get('response_snippet', '')[:200]}...`"
                                ),
                                parse_mode="Markdown"
                            )"""

        new_4 = """                        else:
                            # 🔥 PERBAIKAN #4: Ambil link lengkap
                            complete_link = email_data.get("complete_verification_link", verification_link)

                            await context.bot.send_message(
                                chat_id=chat_id,
                                text=(
                                    "⚠️ *VERIFICATION STATUS UNCLEAR*\\n\\n"
                                    "🔄 *Status: UNKNOWN / AMBIGUOUS*\\n\\n"
                                    f"📧 Email: `{email}`\\n"
                                    f"🎯 SheerID Status: `{sheerid_status}`\\n"
                                    f"📊 HTTP Status: `{click_result.get('status_code')}`\\n\\n"
                                    "🔗 *Link verifikasi lengkap untuk cek manual:*\\n"
                                    f"`{complete_link}`\\n\\n"
                                    "💡 *Cara cek status:*\\n"
                                    "1. Klik link di atas\\n"
                                    "2. Buka di browser (Chrome/Firefox recommended)\\n"
                                    "3. Lihat pesan dari SheerID\\n"
                                    "4. Screenshot jika perlu support\\n\\n"
                                    f"📄 Response preview:\\n"
                                    f"`{click_result.get('response_snippet', '')[:200]}...`"
                                ),
                                parse_mode="Markdown"
                            )"""

        if old_4 in code:
            code = code.replace(old_4, new_4, 1)
            print("✅ Perbaikan #4: UNKNOWN notification - DONE")
        else:
            print("⚠️ Perbaikan #4: Pattern tidak ditemukan")

        # Simpan file yang sudah diperbaiki
        with open('paste_FIXED.txt', 'w', encoding='utf-8') as f:
            f.write(code)

        print("="*70)
        print("✅ SELESAI! File berhasil diperbaiki!")
        print("📁 File baru: paste_FIXED.txt")
        print("="*70)
        print("\n📋 NEXT STEPS:")
        print("1. Rename paste_FIXED.txt jadi paste.txt (atau nama bot kamu)")
        print("2. Upload ke server/Railway")
        print("3. Deploy & test dengan /start")
        print("\n✨ Bot sekarang akan kirim link lengkap di semua error!")

    except FileNotFoundError:
        print("❌ File paste.txt tidak ditemukan!")
        print("💡 Pastikan file paste.txt ada di folder yang sama dengan script ini")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    patch_bot_file()
