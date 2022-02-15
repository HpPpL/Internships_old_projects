namespace Graph
{
    partial class Frm
    {
        /// <summary>
        /// Требуется переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Обязательный метод для поддержки конструктора - не изменяйте
        /// содержимое данного метода при помощи редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.pnl = new System.Windows.Forms.Panel();
            this.btn = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.per_a = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.per_b = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.per_c = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.per_d = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.clr = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // pnl
            // 
            this.pnl.BackColor = System.Drawing.Color.Moccasin;
            this.pnl.Location = new System.Drawing.Point(12, 12);
            this.pnl.Name = "pnl";
            this.pnl.Size = new System.Drawing.Size(600, 600);
            this.pnl.TabIndex = 0;
            this.pnl.Paint += new System.Windows.Forms.PaintEventHandler(this.pnl_Paint);
            // 
            // btn
            // 
            this.btn.Location = new System.Drawing.Point(706, 327);
            this.btn.Name = "btn";
            this.btn.Size = new System.Drawing.Size(191, 83);
            this.btn.TabIndex = 1;
            this.btn.Text = "Построить график";
            this.btn.UseVisualStyleBackColor = true;
            this.btn.Click += new System.EventHandler(this.btn_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 12.25F);
            this.label1.Location = new System.Drawing.Point(702, 62);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(153, 20);
            this.label1.TabIndex = 2;
            this.label1.Text = "Коэффициент A:";
            // 
            // per_a
            // 
            this.per_a.Location = new System.Drawing.Point(706, 85);
            this.per_a.Name = "per_a";
            this.per_a.Size = new System.Drawing.Size(143, 20);
            this.per_a.TabIndex = 3;
            this.per_a.Text = "1";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 12.25F);
            this.label2.Location = new System.Drawing.Point(704, 122);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(154, 20);
            this.label2.TabIndex = 4;
            this.label2.Text = "Коэффициент B:";
            // 
            // per_b
            // 
            this.per_b.Location = new System.Drawing.Point(706, 145);
            this.per_b.Name = "per_b";
            this.per_b.Size = new System.Drawing.Size(142, 20);
            this.per_b.TabIndex = 5;
            this.per_b.Text = "1";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 12.25F);
            this.label3.Location = new System.Drawing.Point(703, 182);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(154, 20);
            this.label3.TabIndex = 6;
            this.label3.Text = "Коэффициент C:";
            // 
            // per_c
            // 
            this.per_c.Location = new System.Drawing.Point(706, 205);
            this.per_c.Name = "per_c";
            this.per_c.Size = new System.Drawing.Size(142, 20);
            this.per_c.TabIndex = 7;
            this.per_c.Text = "0";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Microsoft Sans Serif", 12.25F);
            this.label4.Location = new System.Drawing.Point(704, 243);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(155, 20);
            this.label4.TabIndex = 8;
            this.label4.Text = "Коэффициент D:";
            // 
            // per_d
            // 
            this.per_d.Location = new System.Drawing.Point(708, 275);
            this.per_d.Name = "per_d";
            this.per_d.Size = new System.Drawing.Size(142, 20);
            this.per_d.TabIndex = 9;
            this.per_d.Text = "0";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("Microsoft Uighur", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label5.Location = new System.Drawing.Point(635, 12);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(270, 38);
            this.label5.TabIndex = 10;
            this.label5.Text = "График:|||A*x*x+B*x|-C|-D|";
            // 
            // clr
            // 
            this.clr.Location = new System.Drawing.Point(704, 432);
            this.clr.Name = "clr";
            this.clr.Size = new System.Drawing.Size(193, 82);
            this.clr.TabIndex = 11;
            this.clr.Text = "Отчистить";
            this.clr.UseVisualStyleBackColor = true;
            this.clr.Click += new System.EventHandler(this.clr_Click);
            // 
            // Frm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.Moccasin;
            this.ClientSize = new System.Drawing.Size(992, 749);
            this.Controls.Add(this.clr);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.per_d);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.per_c);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.per_b);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.per_a);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btn);
            this.Controls.Add(this.pnl);
            this.Name = "Frm";
            this.Text = "График";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Panel pnl;
        private System.Windows.Forms.Button btn;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox per_a;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox per_b;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox per_c;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox per_d;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Button clr;
    }
}

