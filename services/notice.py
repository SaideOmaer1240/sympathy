import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email_notificacao(destinatario, assunto, mensagem):
    remetente = "cfilomena@estudantes.unisced.edu.mz"
    senha = "842912694"  # Recomendado usar variáveis de ambiente para segurança

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    corpo = MIMEText(mensagem, 'plain')
    msg.attach(corpo)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg.as_string())
        server.quit()
        print(f"E-mail enviado para {destinatario} com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {str(e)}")

