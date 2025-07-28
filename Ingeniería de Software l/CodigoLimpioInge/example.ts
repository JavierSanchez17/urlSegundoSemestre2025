type PayMethod = 'Mail' | 'Hold' | 'DirectDeposit';
interface Emp {
    id:                           number;
    name:                         string;
    address:                      string;
    
    type:                         'H' | 'S' | 'C'; // H: Hourly, S: Salaried, C: Commissioned
    
    h_rate?:                      number;
    sal?:                         number;
    comm_rate?:                   number;

    lastPaidDate:                 Date;
    pay_method:                   PayMethod;
    
    unionMember?:                 boolean;
    weeklyDues?:                  number;
    pendingServiceCharges?:       number;
}

interface TimeCard {
    date: Date;
    hours: number;
}

interface SalesReceipt {
    date: Date;
    amount: number;
}


class PayrollSystem {
    
    private db: { 
        employees: Emp[], 
        timeCards: { [empId: number]: TimeCard[] }, 
        salesReceipts: { [empId: number]: SalesReceipt[] } 
    };
    
    constructor(database: any) { this.db = database }
    
    public runPayroll(payDateStr: string) {
        const pDate = new Date(payDateStr);
        console.log(`--- Corriendo Nómina para la fecha: ${pDate.toDateString()} ---`);
        for (const emp of this.db.employees) {
            
            
            if (this.isPayDay(emp, pDate)) {
                console.log(`\nCalculando pago para ${emp.name}...`);
                
                let grossPay=this.calculatePay(emp, emp.lastPaidDate, pDate)
                let deductions = this.calculateDeductions(emp, grossPay);
                const netPay = grossPay - deductions;
                
                
                if (netPay > 0) {
                    this.dispatchPayment(emp, netPay);
                    emp.lastPaidDate = pDate; // Actualizar la fecha de último pago
                    if (emp.unionMember) emp.pendingServiceCharges = 0; // Limpiar cargos de servicio
                } else {
                    console.log(`   - Sin pago neto para este período.`);
                }
            }
        }
    }
    

    private calculatePay(emp: Emp, fromDate: Date, toDate: Date): number {
        let result = 0;
        
        if (emp.type === 'H') {
            console.log("   - Empleado por hora.");
            const cards = (this.db.timeCards[emp.id] || []).filter(c => c.date > fromDate && c.date <= toDate);
            for (const card of cards) {
                let payForDay=0;
                if(card.hours>8){
                    const extraHours = card.hours - 8;
                    payForDay=(8*emp.h_rate!)+(extraHours*emp.h_rate!*1.5);
                } else {
                    payForDay = card.hours * emp.h_rate!;
                }
                result+=payForDay;
            }
        } else if (emp.type === 'S') {
            // Un empleado asalariado es pagado su salario completo si es su día de pago.
            console.log("   - Empleado asalariado.");
            result = emp.sal! / 12; // Asumimos que el salario es anual y se paga mensual
        } else if (emp.type === 'C') {
            console.log("   - Empleado con comisión.");
            result = emp.sal! / 12; // Salario base mensual
            const receipts = (this.db.salesReceipts[emp.id] || []).filter(r => r.date > fromDate && r.date <= toDate);
            let commissionTotal = 0;
            receipts.forEach(r => commissionTotal += r.amount * emp.comm_rate!);
            console.log(`   - Comisión adicional: $${commissionTotal.toFixed(2)}`);
            result += commissionTotal;
        }
        
        console.log(`   - Pago Bruto: $${result.toFixed(2)}`);
        return result;
    }
    
    private dispatchPayment(e: Emp, amount: number) {
        const amtStr = amount.toFixed(2);
        
        
        if (e.pay_method === 'Hold') console.log(`   - PAGO: Retener cheque por $${amtStr} para ${e.name}.`);
        else if (e.pay_method === 'Mail') console.log(`   - PAGO: Enviar cheque por $${amtStr} a ${e.address}.`);
        else if (e.pay_method === 'DirectDeposit') console.log(`   - PAGO: Depositar $${amtStr} a la cuenta de ${e.name}.`);
    }
    
    
    private calculateDeductions(emp: Emp, gross: number): number {
        let totalDeductions = 0
        if (emp.unionMember) {
            const numWeeks = 4; // Simplificación
            const dues = emp.weeklyDues! * numWeeks;
            const serviceCharges = emp.pendingServiceCharges || 0;
            totalDeductions = dues + serviceCharges;
            console.log(`   - Deducciones del Sindicato: $${totalDeductions.toFixed(2)} (Cuotas: $${dues}, Cargos: $${serviceCharges})`);
        }
        return totalDeductions;
    }
    
    
    private isPayDay(emp: Emp, date: Date): boolean {
        const dayOfWeek = date.getDay(); // 0=Domingo, 6=Sábado
        if (emp.type === 'H') { return dayOfWeek === 5; /* Viernes */ }
        else if (emp.type === 'S') { 
            const nextDay = new Date(date); nextDay.setDate(date.getDate() + 1); return nextDay.getMonth() !== date.getMonth(); // Es el último día del mes
        }
        else if (emp.type === 'C') { 
            const firstFriday = new Date(date.getFullYear(), 0, 1);
            while (firstFriday.getDay() !== 5) { firstFriday.setDate(firstFriday.getDate() + 1); }
            const diffTime = Math.abs(date.getTime() - firstFriday.getTime()); const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)); return dayOfWeek === 5 && (Math.floor(diffDays / 7) % 2 === 1);
        }
        return false;
    }
}


// --- DEMOSTRACIÓN ---

const testDB = {
    employees: [
        { id: 1, name: 'John Doe', address: '123 Main St', type: 'H', h_rate: 25, lastPaidDate: new Date('2023-10-20'), pay_method: 'Hold', unionMember: true, weeklyDues: 10, pendingServiceCharges: 5.50 },
        { id: 2, name: 'Jane Smith', address: '456 Oak Ave', type: 'S', sal: 60000, lastPaidDate: new Date('2023-09-30'), pay_method: 'DirectDeposit' },
        { id: 3, name: 'Peter Jones', address: '789 Pine Ln', type: 'C', sal: 48000, comm_rate: 0.10, lastPaidDate: new Date('2023-10-13'), pay_method: 'Mail', unionMember: true, weeklyDues: 15 }
    ],
    timeCards: {
        1: [
            new TimeCard({ date: new Date('2023-10-23'), hours: 8 }),
            new TimeCard({ date: new Date('2023-10-24'), hours: 9 }), // 1hr overtime
            new TimeCard({ date: new Date('2023-10-25'), hours: 8 }),
            new TimeCard({ date: new Date('2023-10-26'), hours: 10 }), // 2hr overtime
            new TimeCard({ date: new Date('2023-10-27'), hours: 8 }),
        ]
    },
    salesReceipts: {
        3: [
            new SalesReceipt({ date: new Date('2023-10-18'), amount: 500 }),
            new SalesReceipt({ date: new Date('2023-10-25'), amount: 1200 }),
        ]
    }
};

function runApplication() {
    const payrollApp = new PayrollSystem(testDB);
    
    // Simular la ejecución diaria durante una semana.
    payrollApp.runPayroll('2023-10-27'); // Viernes, día de pago para John y Peter
    console.log("=====================================================");
    payrollApp.runPayroll('2023-10-31'); // Fin de mes, día de pago para Jane
}

runApplication();